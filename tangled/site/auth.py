import logging

import bcrypt

from .model import User


log = logging.getLogger(__name__)


def get_canonical_user_id(request, user_id):
    """Get canonical user ID.

    ``user_id`` can be an ID, an email a

    ``None`` is returned to indicate that the user doesn't exit.

    """
    if user_id is None:
        return None
    q = request.db_session.query(User.id)
    if isinstance(user_id, int):
        return q.filter_by(id=user_id).scalar()
    else:
        user_id = user_id.strip().lower()
        # Check by email
        canonical_id = q.filter_by(email=user_id).scalar()
        if canonical_id is not None:
            log.debug('Found user {} by email address'.format(canonical_id))
            return canonical_id
        # Check by username
        canonical_id = q.filter_by(username=user_id).scalar()
        if canonical_id is not None:
            log.debug('Found user {} by username'.format(canonical_id))
            return canonical_id
    log.debug('User does not exist: {}'.format(user_id))


def user_id_validator(request, user_id):
    """Ensure user (still) exists and return canonical ID."""
    assert isinstance(user_id, int), user_id
    return get_canonical_user_id(request, user_id)


def check_credentials(request, user_id, plain_text_password):
    user_id = get_canonical_user_id(request, user_id)
    if user_id is None:
        log.debug('Unknown user: {}'.format(user_id))
        return None
    plain_text_password = plain_text_password.encode('utf-8')
    q = request.db_session.query(User.password)
    q = q.filter_by(id=user_id)
    hashed_password = q.scalar()
    if bcrypt.hashpw(plain_text_password, hashed_password) == hashed_password:
        log.debug('Valid credentials')
        return user_id
    log.debug('Invalid credentials')


def sign_up(request, email, plain_text_password, username=None):
    if get_canonical_user_id(request, email):
        log.debug('User exists with email: {}'.format(email))
        return None
    if get_canonical_user_id(request, username):
        log.debug('User exists with username: {}'.format(username))
        return None
    hashed_password = hash_password(plain_text_password)
    user = User(email=email, password=hashed_password, username=username)
    request.db_session.add(user)
    request.db_session.flush([user])
    return user.id


def hash_password(plain_text_password):
    """Return salted, hashed version of plain text password."""
    plain_text_password = plain_text_password.encode('utf-8')
    hashed_password = bcrypt.hashpw(plain_text_password, bcrypt.gensalt())
    return hashed_password


def has_permission(request, user_id, permission):
    user = request.db_session.query(User).get(user_id)
    return user is not None and user.has_permission(permission)

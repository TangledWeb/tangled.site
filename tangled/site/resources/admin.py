from tangled.web import Resource, represent

from ..model import User


@represent('*/*', permission='admin')
class Users(Resource):

    @represent('text/html', template_name='admin/users.mako')
    def GET(self):
        q = self.request.db_session.query(User)
        users = q.all()
        return {
            'users': users,
        }

from tangled.web import Resource, represent

from .. import model


class User(Resource):

    @represent('*/*', permission='delete_user', status=303, location='REFERER')
    def DELETE(self):
        req = self.request
        user = req.db_session.query(model.User).get(self.urlvars['id'])
        if user.id == req.user.id:
            req.flash(
                "You can't delete your own account while you are signed in")
            req.abort(400)
        else:
            req.db_session.delete(user)


@represent('*/*', requires_authentication=True, status=303)
class UserActions(Resource):

    def POST(self):
        req = self.request
        action = self.urlvars['action'].replace('-', '_')
        action = getattr(self, action, None)
        if action is None:
            req.abort(404)
        return action(self, req)

    def update_email_address(self):
        pass


@represent('*/*', requires_authentication=True)
class Profile(Resource):

    @represent('text/html', template_name='profile.mako')
    def GET(self):
        return {}

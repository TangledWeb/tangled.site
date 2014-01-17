from tangled.web import Resource, config

from ..model import User


@config('*/*', permission='admin')
class Users(Resource):

    @config('text/html', template_name='admin/users.mako')
    def GET(self):
        q = self.request.db_session.query(User)
        users = q.all()
        return {
            'users': users,
        }

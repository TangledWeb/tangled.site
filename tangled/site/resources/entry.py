from webob.exc import HTTPNotFound

from tangled.web import Resource, represent

from .. import model


class Entries(Resource):

    @represent('text/html', template_name='entries.mako')
    def GET(self):
        session = self.request.db_session
        entries = session.query(model.Entry).all()
        return {
            'entries': entries,
        }

    @represent('*/*', permission='create_entry')
    @represent('text/html', status=303)
    def POST(self):
        """Create a new entry."""
        session = self.request.db_session
        new_entry = model.Entry(**self.request.params)
        session.add(new_entry)
        session.flush()
        location = self.request.make_url('/entry/{0.id}'.format(new_entry))
        self.request.response.location = location


class NewEntry(Resource):

    @represent('text/html', template_name='new-entry.mako')
    def GET(self):
        return {
            'entry': model.Entry(),
        }


class Entry(Resource):

    @represent('text/html', template_name='entry.mako')
    def GET(self):
        id = int(self.urlvars['id'])
        session = self.request.db_session
        entry = session.query(model.Entry).get(id)
        if not entry:
            raise HTTPNotFound()
        return {
            'entry': entry,
        }

    @represent('*/*', permission='edit_entry')
    @represent('text/html', status=303)
    def PUT(self):
        pass

    @represent('*/*', permission='delete_entry')
    @represent('text/html', status=303)
    def DELETE(self):
        entry = self.GET()['entry']
        self.request.db_session.delete(entry)
        location = self.request.make_url('/entries')
        self.request.response.location = location


class EditEntry(Resource):

    @represent('text/html', template_name='edit_entry.mako')
    def GET(self):
        return {
            'entry': Entry(self.app, self.request).GET()['entry'],
        }

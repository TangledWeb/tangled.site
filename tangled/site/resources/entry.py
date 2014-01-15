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
        location = self.request.resource_url('entry', {'id': new_entry.id})
        self.request.response.location = location


@represent('*/*', permission='create_entry')
class NewEntry(Resource):

    @represent('text/html', template_name='new_entry.mako')
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
            self.request.abort(404)
        return {
            'entry': entry,
        }

    @represent('*/*', permission='edit_entry')
    @represent('text/html', status=303)
    def PUT(self):
        req = self.request
        resource = Entry(self.app, req, self.name, self.urlvars)
        entry = resource.GET()['entry']
        entry.title = req.POST['title']
        entry.content = req.POST['content']
        req.response.location = resource.url()

    # @represent('*/*', permission='delete_entry')
    @represent('text/html', status=303)
    def DELETE(self):
        entry = self.GET()['entry']
        self.request.db_session.delete(entry)
        location = self.request.resource_url('entries')
        self.request.response.location = location


@represent('*/*', permission='edit_entry')
class EditEntry(Resource):

    @represent('text/html', template_name='edit_entry.mako')
    def GET(self):
        resource = Entry(self.app, self.request, self.name, self.urlvars)
        entry = resource.GET()['entry']
        return {
            'entry': entry,
        }

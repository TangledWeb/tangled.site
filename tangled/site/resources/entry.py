from sqlalchemy.orm.exc import NoResultFound

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
        req = self.request
        content = req.POST['content']
        kwargs = dict(
            slug=req.POST['slug'],
            title=req.POST['title'],
            content=content,
        )
        new_entry = model.Entry(**kwargs)
        session = req.db_session
        session.add(new_entry)
        session.flush()
        location = req.resource_url('entry', {'id': new_entry.id})
        req.response.location = location


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
        id = self.urlvars['id']
        session = self.request.db_session
        q = session.query(model.Entry)
        entry = q.get(id)
        if entry is None:
            try:
                entry = q.filter_by(slug=id).one()
            except NoResultFound:
                self.request.abort(404)
        return {
            'entry': entry,
        }

    @represent('*/*', permission='edit_entry')
    @represent('text/html', status=303)
    def PUT(self):
        req = self.request
        entry = self.GET()['entry']
        entry.slug = req.POST['slug']
        entry.title = req.POST['title']
        entry.content = req.POST['content']
        req.response.location = self.url()

    @represent('*/*', permission='delete_entry')
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
        resource = Entry(self.app, self.request, urlvars=self.urlvars)
        entry = resource.GET()['entry']
        return {
            'entry': entry,
        }

from sqlalchemy.orm.exc import NoResultFound

from tangled.web import Resource, config

from .. import model


class Entries(Resource):

    @config('text/html', template_name='entries.mako')
    def GET(self):
        session = self.request.db_session
        entries = session.query(model.Entry).all()
        return {
            'entries': entries,
        }

    @config('*/*', permission='create_entry')
    @config('text/html', status=303)
    def POST(self):
        """Create a new entry."""
        req = self.request
        content = req.POST['content']
        kwargs = dict(
            slug=req.POST['slug'],
            title=req.POST['title'],
            is_page=('is_page' in req.POST),
            content=content,
        )
        new_entry = model.Entry(**kwargs)
        session = req.db_session
        session.add(new_entry)
        session.flush()
        location = req.resource_url('entry', {'id': new_entry.id})
        req.response.location = location


@config('*/*', permission='create_entry')
class NewEntry(Resource):

    @config('text/html', template_name='new_entry.mako')
    def GET(self):
        return {
            'entry': model.Entry(),
        }


class Entry(Resource):

    @config('text/html', template_name='entry.mako')
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

    @config('*/*', permission='edit_entry')
    @config('text/html', status=303)
    def PUT(self):
        req = self.request
        entry = self.GET()['entry']
        entry.slug = req.POST['slug']
        entry.title = req.POST['title']
        entry.is_page = 'is_page' in req.POST
        entry.content = req.POST['content']
        req.response.location = self.url()

    @config('*/*', permission='delete_entry')
    @config('text/html', status=303)
    def DELETE(self):
        entry = self.GET()['entry']
        self.request.db_session.delete(entry)
        location = self.request.resource_url('entries')
        self.request.response.location = location


@config('*/*', permission='edit_entry')
class EditEntry(Resource):

    @config('text/html', template_name='edit_entry.mako')
    def GET(self):
        resource = Entry(self.app, self.request, urlvars=self.urlvars)
        entry = resource.GET()['entry']
        return {
            'entry': entry,
        }

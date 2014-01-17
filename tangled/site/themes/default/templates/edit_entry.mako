<%inherit file="base.mako"/>

<%block name="page_title">Edit Entry</%block>

<%block name="content">
    <form method="POST" action="${request.resource_url('entry', {'id': entry.id})}">
      ${request.csrf_tag}
      <input type="hidden" name="$method" value="PUT" />

      <fieldset>
        <label for="entry.slug">Slug</label>
        <input type="text" id="entry.slug" name="slug" size="30" value="${entry.slug}" />

        <label for="entry.title">Title</label>
        <input type="text" id="entry.title" name="title" size="30" value="${entry.title}" />

        <label for="entry.is_page">Page?</label>
        <input type="checkbox" id="entry.is_page" name="is_page" ${'checked="checked"' if entry.is_page else ''} />

        <label for="entry.content">Content</label>
        <textarea id="entry.content" name="content" cols="80" rows="25">${entry.content}</textarea>

        <input type="submit" value="Update" />
      </fieldset>
    </form>

    <br />

    <form method="POST" action="${request.resource_url('entry', {'id': entry.id})}">
      ${request.csrf_tag}
      <input type="hidden" name="$method" value="DELETE" />
      <fieldset>
        <input type="submit" value="Delete" />
      </fieldset>
    </form>
</%block>

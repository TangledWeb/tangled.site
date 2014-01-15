<%inherit file="base.mako"/>

<%block name="page_title">
  <h2>Edit Entry</h2>
</%block>

<%block name="content">
    <form method="POST" action="${request.resource_url('entry', {'id': entry.id})}">
      ${request.csrf_tag | n}
      <input type="hidden" name="$method" value="PUT" />

      <fieldset>
        <label for="title">Slug</label>
        <input type="text" name="slug" value="${entry.slug}"/>

        <label for="title">Title</label>
        <input type="text" name="title" value="${entry.title}" />

        <label for="content">Content</label>
        <textarea name="content">${entry.content}</textarea>
      </fieldset>

      <input type="submit" value="Update" />
    </form>
</%block>

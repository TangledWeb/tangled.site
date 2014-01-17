<%inherit file="base.mako"/>

<%block name="page_title">New Entry</%block>

<%block name="content">
    <form method="POST" action="${request.make_path('/entries')}">
      ${request.csrf_tag}

      <fieldset>
        <label for="entry.slug">Slug</label>
        <input type="text" id="entry.slug" name="slug" size="30" />

        <label for="entry.title">Title</label>
        <input type="text" id="entry.title" name="title" size="30" />

        <label for="entry.is_page">Page?</label>
        <input type="checkbox" id="entry.is_page" name="is_page" />

        <label for="entry.content">Content</label>
        <textarea id="entry.content" name="content" cols="80" rows="25"></textarea>
      </fieldset>

      <input type="submit" value="Create new entry" />
    </form>
</%block>

<%inherit file="base.mako"/>

<%block name="page_title">New Entry</%block>

<%block name="content">
    <form method="POST" action="${request.make_path('/entries')}">
      ${request.csrf_tag | n}

      <fieldset>
        <label for="title">Slug</label>
        <input type="text" name="slug" size="30" />

        <label for="title">Title</label>
        <input type="text" name="title" size="30" />

        <label for="content">Content</label>
        <textarea name="content" cols="80" rows="25"></textarea>
      </fieldset>

      <input type="submit" value="Create new entry" />
    </form>
</%block>

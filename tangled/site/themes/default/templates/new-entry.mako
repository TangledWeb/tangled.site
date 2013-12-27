<%inherit file="base.mako"/>

<%block name="page_title">
  <h2>New Entry</h2>
</%block>

<%block name="content">
    <form method="POST" action="${request.make_path('/entries')}">
      ${request.csrf_tag | n}
      <input type="text" name="title" />
      <input type="submit" value="Create new entry" />
    </form>
</%block>

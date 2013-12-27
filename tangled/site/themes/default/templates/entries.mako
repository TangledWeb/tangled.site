<%inherit file="base.mako"/>

<%block name="page_title">
  <h2>Entries</h2>
</%block>

<%block name="content">
  % for entry in entries:
    <h3><a href="/entry/${entry.id}">${entry.title}</a></h3>
    <div>${entry.content}</div>
  % endfor
</%block>
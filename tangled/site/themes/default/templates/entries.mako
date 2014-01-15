<%inherit file="base.mako"/>

<%block name="page_title">Entries</%block>

<%block name="content">
  % for entry in entries:
    <h3><a href="/entry/${entry.id}">${entry.title}</a></h3>
    <div>${entry.content_html | n}</div>
  % endfor
</%block>

% if request.user:
  <ul class="nav">
    % if request.user.has_permission('new_entry'):
      <li>
        <a href="${request.resource_url('new_entry')}">New Entry</a>
      </li>
    % endif
  </ul>
% endif

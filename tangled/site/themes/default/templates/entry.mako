<%inherit file="base.mako"/>

<%block name="page_title">${entry.title}</%block>

<%block name="content">
  <div>${entry.content}</div>
  % if request.user and request.user.has_role('admin'):
    <p>
      <small>
        Created: ${request.helpers.format_datetime(entry.created_at)}<br/>
        Updated: ${request.helpers.format_datetime(entry.updated_at)}<br/>
      </small>
    </p>
  % endif
</%block>

% if request.user:
  <ul class="nav">
    % if request.user.has_permission('edit_entry'):
      <li>
        <a href="${request.resource_url('edit_entry', {'id': entry.id})}">Edit</a>
      </li>
    % endif
    % if request.user.has_permission('delete_entry'):
      <li>
        <form method="POST" action="${request.resource_url('entry', {'id': entry.id})}">
          ${request.csrf_tag | n}
          <input type="hidden" name="$method" value="DELETE">
          <input type="submit" value="Delete" />
        </form>
      </li>
    % endif
  </ul>
% endif

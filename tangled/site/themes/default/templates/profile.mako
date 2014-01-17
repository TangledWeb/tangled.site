<%inherit file="base.mako"/>

<%block name="page_title">Your Profile</%block>

<%def name="put_form(legend=None, submit_value=None)">
  <% form_action = request.resource_url('user', {'id': user.id}) %>
  <form method="post" action="${form_action}">
    ${request.csrf_tag}
    <input type="hidden" name="$method" value="PUT" />
    <fieldset>
      % if legend:
        <legend>${legend}</legend>
      % endif
      ${caller.body()}
      <input type="submit" value="${submit_value or 'Update'}" />
    </fieldset>
  </form>
  <br />
</%def>

<%block name="content">
  <%self:put_form legend="Name">
    <input type="text" name="user.name" value="${user.name or ''}" />
  </%self:put_form>

  <%self:put_form legend="Username">
    <input type="text" name="user.username" value="${user.username or ''}" />
  </%self:put_form>

  <%self:put_form legend="Email Address">
    <input type="text" name="user.email" value="${user.email}" />
  </%self:put_form>

  <%self:put_form legend="Change Password" submit_value="Change Password">
    <label for="user.current_password">Current password</label>
    <input type="password" id="user.current_password" name="user.current_password" />

    <label for="user.password">New password</label>
    <input type="password" id="user.password" name="user.password" />

    <label for="user.confirm_password">New password</label>
    <input type="password" id="user.confirm_password" name="user.confirm_password" />
  </%self:put_form>
</%block>

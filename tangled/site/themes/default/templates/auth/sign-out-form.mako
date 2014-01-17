<%def name="sign_out_form()">
  <form method="POST" action="${request.make_path('/sign-out')}">
    ${request.csrf_tag}
    <input type="submit" value="Sign Out" />
  </form>
</%def>

from time import sleep


class TestPages(object):

    """
    Test Definition Layer
    """

    def test_main_page(self, username, password):
        assert self.main_page.github_logo.is_displayed(), "GitHub Logo is not shown"
        assert self.main_page.sing_up_form.is_displayed(), "The sing up form isn't displayed"

    def test_login_process_with_invalid_credential(self, username, password):
        login_page = self.main_page.click_on_sing_in_button()

        assert login_page.github_logo.is_displayed(), "GitHub Logo is not shown"
        assert login_page.login_form.is_displayed(), "Login form is not shown"
        assert login_page.username_field.is_displayed(), "Username input field is not shown"
        assert login_page.password_field.is_displayed(), "Password field is not shown"
        assert login_page.sing_in_button.is_displayed(), "Sing in button is not shown"

        username = "abracadabre@mail.com"
        password = "123e12er13r"
        login_error = login_page.enter_login(username) \
            .enter_password(password) \
            .click_on_login_button_with_invalid_credential()

        assert login_error.error_message[0].is_displayed(), "The error message isn't appeared"

    def test_login_process_with_valid_credential(self, username, password):
        login_page = self.main_page.click_on_sing_in_button()

        assert login_page.github_logo.is_displayed(), "GitHub Logo is not shown"
        assert login_page.login_form.is_displayed(), "Login form is not shown"
        assert login_page.username_field.is_displayed(), "Username input field is not shown"
        assert login_page.password_field.is_displayed(), "Password field is not shown"
        assert login_page.sing_in_button.is_displayed(), "Sing in button is not shown"

        user_workspace = login_page.enter_login(username) \
            .enter_password(password) \
            .click_on_login_button()

        assert user_workspace.github_logo.is_displayed(), "GitHub Logo is not shown"
        assert user_workspace.user_avatar.is_displayed(), "User avatar is not displayed"
        assert user_workspace.start_a_project_button.is_displayed(), "Start a project button is not shown"

    def test_create_new_project(self, username, password):
        login_page = self.main_page.click_on_sing_in_button()

        user_workspace_page = login_page.enter_login(username) \
            .enter_password(password) \
            .click_on_login_button()
        new_project = user_workspace_page.click_on_create_new_project()
        assert new_project.github_logo.is_displayed(), "GitHub Logo is not shown"
        assert new_project.create_repository_inscription.is_displayed(), "The Create a new repository inscription " \
                                                                         "does not appear "
        assert new_project.create_repository_button.is_displayed(), "The Create Repository button isn't shown"

    def test_crate_new_repository(self, username, password):
        login_page = self.main_page.click_on_sing_in_button()

        user_workspace_page = login_page.enter_login(username) \
            .enter_password(password) \
            .click_on_login_button()
        new_project = user_workspace_page.click_on_create_new_project()
        new_project.name_of_repository()
        repository_page = new_project.click_on_create_repository_button()
        sleep(5)
        assert repository_page.github_logo.is_displayed(), "GitHub Logo is not shown"
        assert repository_page.repository_name.is_displayed(), "Repository name is not displayed"
        assert repository_page.read_the_guide_button.is_displayed(), "Read the guide button is not displayed"

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from kolibri.core.auth.constants.user_kinds import ANONYMOUS
from kolibri.core.hooks import NavigationHook
from kolibri.core.hooks import RoleBasedRedirectHook
from kolibri.core.webpack import hooks as webpack_hooks
from kolibri.plugins.base import KolibriPluginBase


class User(KolibriPluginBase):
    translated_view_urls = "urls"


class UserAsset(webpack_hooks.WebpackBundleHook):
    unique_slug = "user_module"


class LogInRedirect(RoleBasedRedirectHook):
    role = ANONYMOUS

    @property
    def url(self):
        return self.plugin_url(User, "user")


class LogInNavAction(NavigationHook, webpack_hooks.WebpackBundleHook):
    unique_slug = "user_module_login_nav_side_nav"


class ProfileNavAction(NavigationHook, webpack_hooks.WebpackBundleHook):
    unique_slug = "user_module_user_profile_nav_side_nav"

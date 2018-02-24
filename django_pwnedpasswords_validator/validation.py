# -*- coding: utf-8 -*-

# Copyright 2018 Lionheart Software LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import pwnedpasswords

class PwnedPasswordValidator(object):
    ERROR_TEXT = _("This password has previously appeared in a data breach and should not be used.")

    def __init__(self, error_text=ERROR_TEXT, anonymous=True):
        self.anonymous = anonymous
        self.error_text = error_text

    def validate(self, password, user=None):
        count = pwnedpasswords.check(password, anonymous=self.anonymous)
        if count > 0:
            raise ValidationError(_(self.error_text), code="password_is_pwned")

    def get_help_text(self):
        return  _("Your password has previously appeared in a data breach and should never be used.")

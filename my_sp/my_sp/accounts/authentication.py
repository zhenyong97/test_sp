from djangosaml2.backends import Saml2Backend


class ModifiedSaml2Backend(Saml2Backend):
    def save_user(self, user, *args, **kwargs):
        print("========================")
        user.save()
        return super().save_user(user, *args, **kwargs)
    
    def _update_user(self, user, attributes: dict, attribute_mapping: dict, force_save: bool = False):
        print("-------------------------")
        print(attributes)
        if 'eduPersonEntitlement' in attributes:
            if 'some-entitlement' in attributes['eduPersonEntitlement']:
                user.is_staff = True
                force_save = True
            else:
                user.is_staff = False
                force_save = True
        return super()._update_user(user, attributes, attribute_mapping, force_save)
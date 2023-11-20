import saml2
from saml2.saml import  NAMEID_FORMAT_UNSPECIFIED, NAME_FORMAT_BASIC
from saml2.sigver import get_xmlsec_binary
from .settings import DEBUG, BASE_DIR
import os

SAML_ENTITY_URL = 'http://localhost:8000/saml2'

CONFIG = {
    'debug' : DEBUG,
    'xmlsec_binary': get_xmlsec_binary(['/usr/bin/xmlsec1']),
    'entityid': '{}/metadata'.format(SAML_ENTITY_URL),

    'service': {
        'sp': {
            'name': 'Django SAML2 SP',
            'endpoints': {
                'assertion_consumer_service': [
                    ('{}/acs/'.format(SAML_ENTITY_URL), saml2.BINDING_HTTP_POST)
                ],
                'single_sign_on_service': [
                    ('{}/ls/post'.format(SAML_ENTITY_URL), saml2.BINDING_HTTP_POST),
                    ('{}/ls/redirect'.format(SAML_ENTITY_URL), saml2.BINDING_HTTP_REDIRECT),
                ],
            },
            'name_id_format': [NAMEID_FORMAT_UNSPECIFIED],
            'authn_requests_signed': True,
            'want_assertions_signed': True,
            'allow_unsolicited': True,
             # attributes that this project need to identify a user
            'required_attributes': ['PartnerSlug',
                                  'Email',
                                  'FirstName','LastName'],

            # attributes that may be useful to have but not required
            'optional_attributes': ['MemberLevel'],
            'requested_attribute_name_format': NAME_FORMAT_BASIC
        },
    },

    'attribute_map_dir': os.path.join(BASE_DIR, 'accounts/saml2attribute_maps'),
    'metadata': {
        'local': [os.path.join(BASE_DIR, 'accounts/idp/idp_metadata.xml')],
        'remote': ['https://samltest.id/saml/idp']
    },

    # Signing
    'key_file': BASE_DIR / '/accounts/certificates/private.key',
    'cert_file': BASE_DIR / '/accounts/certificates/public.cert',
    # Encryption
    'encryption_keypairs': [{
        'key_file': BASE_DIR / '/accounts/certificates/private.key',
        'cert_file': BASE_DIR / '/accounts/certificates/public.cert',
    }],
    'valid_for': 365 * 24, 
}

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.statusmessages.interfaces import IStatusMessage
from plone.app.contenttypes.migration.migration import migrateCustomAT


class MyMigration(BrowserView):

    template = ViewPageTemplateFile('crgis_migration.pt')
    at_metadata_fields = ATContentTypeSchema.keys()
    dx_metadata_fields = list(at_metadata_fields)
    # some metadata names are different between AT and DX...
    dx_metadata_fields.remove('allowDiscussion')
    dx_metadata_fields.remove('excludeFromNav')
    dx_metadata_fields.append('allow_discussion')
    dx_metadata_fields.append('exclude_from_nav')

    def __call__(self):
        results = self.migrate()
        messages = IStatusMessage(self.request)
        for migration_result in results:
            res_type = migration_result.get('type')
            res_infos = migration_result.get('infos')
            if res_infos.get('errors'):
                messages.add(
                    u'Error when migration "%s" type. Check the '
                    u'log for other informations.'
                    % res_type, type=u"error")
            else:
                msg = u'Migration applied successfully for %s "%s" items.' \
                      % (res_infos.get('counter'), res_type)
                messages.add(msg, type=u"info")
        return self.index()
 
    def migrate(self, dry_run=False):
        '''We will build a dict like :
           {'MyATPortalType':
                {'MyDXPortalType': (
                    {'AT_field_name': 'fieldname1',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'field_name1',
                     'DX_field_type': 'RichText'}, )}}
        Call the migrateCustomAT migrator for each AT content_type we choose
        to migrate.
        '''
        data = {
            'Temple':
                {'target_type': 'Temple',
                 'field_mapping': [
                    {'AT_field_name': 'data_src',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'data_src',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'coordinate',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'coordinate',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'facing',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'facing',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'deity_host',
                     'AT_field_type': 'Products.Archetypes.Field.LinesField',
                     'DX_field_name': 'deity_host',
                     'DX_field_type': 'Tuple'},
                    {'AT_field_name': 'deity_host_o',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'deity_host_o',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'deity_host_a',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'deity_host_a',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'deity_company',
                     'AT_field_type': 'Products.Archetypes.Field.LinesField',
                     'DX_field_name': 'deity_company',
                     'DX_field_type': 'Tuple'},
                    {'AT_field_name': 'religion',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'religion',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'religion_o',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'religion_o',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'building',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'building',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'building_o',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'building_o',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'registered',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'registered',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'funding',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'funding',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'organizing',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'organizing',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'organizing_o',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'organizing_o',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'address',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'address',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'in_charge',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'in_charge',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'tel',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'tel',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'homepage',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'homepage',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'era',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'era',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'era_end',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'era_end',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'year_accuracy',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'year_accuracy',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'history',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'year_accuracy',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'era_1',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'era_1',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'era_2',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'era_2',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'era_ref',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'era_ref',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'deity_accompany',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'deity_accompany',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'worship',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'worship',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'introduction',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'introduction',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'overview',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'overview',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'antiquity',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'antiquity',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'narrate',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'narrate',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'non_narrate',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'non_narrate',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'academic',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'academic',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'literature',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'literature',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'fill_in',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'fill_in',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'fill_date',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'fill_date',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'jstq',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'jstq',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'jstq_o',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'jstq_o',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'jsfw',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'jsfw',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'xyfw',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'xyfw',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'flxt',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'flxt',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'flxt_o',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'flxt_o',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'ymmy',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'ymmy',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'ymmy_o',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'ymmy_o',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'xhly',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'xhly',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'xhly_o',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'xhly_o',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'nlqs',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'nlqs',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'nlqs_o',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'nlqs_o',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'wyxx',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'wyxx',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'wyxx_o',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'wyxx_o',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'medicine',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'medicine',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'luck',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'luck',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'organization',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'organization',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'desc_o',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'desc_o',
                     'DX_field_type': 'RichText'}
                 ]
                },
            'BiXieWu':
                {'target_type': 'BiXieWu',
                 'field_mapping': [
                    {'AT_field_name': 'data_src',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'data_src',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'lct_cou',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'lct_cou',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'lct_tow',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'lct_tow',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'lct_vil',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'lct_vil',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'coordinate',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'coordinate',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'type',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'btype',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'era',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'era',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'era_ref',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'era_ref',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'facing',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'facing',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'material',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'material',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'volumn',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'volumn',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'locational',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'locational',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'purpose',
                     'AT_field_type': 'Products.Archetypes.Field.LinesField',
                     'DX_field_name': 'purpose',
                     'DX_field_type': 'Tuple'},
                    {'AT_field_name': 'worship',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'worship',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'establishment',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'establishment',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'spatial',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'spatial',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'environment',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'environment',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'reference',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'reference',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'remark',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'remark',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'r_temples',
                     'AT_field_type': 'Products.Archetypes.Field.ReferenceField',
                     'DX_field_name': 'r_temples',
                     'DX_field_type': 'RelationList'},
                    {'AT_field_name': 'village',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'village',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'color',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'color',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'genre',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'genre',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'posture',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'posture',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'gender',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'gender',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'shi_d',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'shi_d',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'shi_w',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'shi_w',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'shi_h',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'shi_h',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'shi_t',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'shi_t',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'base_l',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'base_l',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'base_w',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'base_w',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'base_h',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'base_h',
                     'DX_field_type': 'StringField'}
                 ]
                },
            'Photo':
                {'target_type': 'Photo',
                 'field_mapping': [
                    {'AT_field_name': 'image',
                     'AT_field_type': 'Products.Archetypes.Field.ImageField',
                     'DX_field_name': 'image',
                     'DX_field_type': 'NamedBlobImage'},
                    {'AT_field_name': 'category',
                     'AT_field_type': 'Products.Archetypes.Field.LinesField',
                     'DX_field_name': 'category',
                     'DX_field_type': 'Tuple'},
                    {'AT_field_name': 'attachesTo',
                     'AT_field_type': 'Products.Archetypes.Field.LinesField',
                     'DX_field_name': 'attachesTo',
                     'DX_field_type': 'Tuple'},
                    {'AT_field_name': 'cou',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'cou',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'tow',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'tow',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'vil',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'vil',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'lng',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'lng',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'lat',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'lat',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'year',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'year',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'month',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'month',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'day',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'day',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'owner_name',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'owner_name',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'owner_org',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'owner_org',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'owner_title',
                     'AT_field_type': 'Products.Archetypes.Field.StringField',
                     'DX_field_name': 'owner_title',
                     'DX_field_type': 'StringField'},
                    {'AT_field_name': 'reference',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'reference',
                     'DX_field_type': 'RichText'}
                 ]
                },
            'Pilgrimage':
                {'target_type': 'Pilgrimage',
                 'field_mapping': [
                    {'AT_field_name': 'body',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'body',
                     'DX_field_type': 'RichText'}
                 ]
                },
            'Schedule':
                {'target_type': 'Schedule',
                 'field_mapping': [
                    {'AT_field_name': 'body',
                     'AT_field_type': 'Products.Archetypes.Field.TextField',
                     'DX_field_name': 'body',
                     'DX_field_type': 'RichText'},
                    {'AT_field_name': 'temples',
                     'AT_field_type': 'Products.Archetypes.Field.ReferenceField',
                     'DX_field_name': 'temples',
                     'DX_field_type': 'RelationList'}
                 ]
                }
        }

        # now that the data dict contains relevant information, we can call
        # the custom migrator
        migration_results = []
        for at_typename in data:
            fields_mapping = data[at_typename]['field_mapping']
            res = migrateCustomAT(
                fields_mapping=fields_mapping,
                src_type=at_typename,
                dst_type=data[at_typename]['target_type'],
                dry_run=dry_run)
            migration_results.append({'type': at_typename,
                                      'infos': res})
        return migration_results


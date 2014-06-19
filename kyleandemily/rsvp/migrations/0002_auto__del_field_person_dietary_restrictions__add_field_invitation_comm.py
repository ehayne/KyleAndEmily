# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Person.dietary_restrictions'
        db.delete_column(u'rsvp_person', 'dietary_restrictions')

        # Adding field 'Invitation.comment'
        db.add_column(u'rsvp_invitation', 'comment',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=2000, blank=True),
                      keep_default=False)

        # Adding field 'Invitation.song'
        db.add_column(u'rsvp_invitation', 'song',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Invitation.plusOne'
        db.add_column(u'rsvp_invitation', 'plusOne',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Person.dietary_restrictions'
        db.add_column(u'rsvp_person', 'dietary_restrictions',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Deleting field 'Invitation.comment'
        db.delete_column(u'rsvp_invitation', 'comment')

        # Deleting field 'Invitation.song'
        db.delete_column(u'rsvp_invitation', 'song')

        # Deleting field 'Invitation.plusOne'
        db.delete_column(u'rsvp_invitation', 'plusOne')


    models = {
        u'rsvp.invitation': {
            'Meta': {'object_name': 'Invitation'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'plusOne': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'responded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'song': ('django.db.models.fields.TextField', [], {'max_length': '200', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'rsvp.person': {
            'Meta': {'object_name': 'Person'},
            'attending': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invitation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'people'", 'to': u"orm['rsvp.Invitation']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rsvp']
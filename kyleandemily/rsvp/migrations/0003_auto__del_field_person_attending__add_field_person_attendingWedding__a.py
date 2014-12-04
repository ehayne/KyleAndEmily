# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Person.attending'
        db.delete_column(u'rsvp_person', 'attending')

        # Adding field 'Person.attendingWedding'
        db.add_column(u'rsvp_person', 'attendingWedding',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.attendingWelcome'
        db.add_column(u'rsvp_person', 'attendingWelcome',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.attendingFarewell'
        db.add_column(u'rsvp_person', 'attendingFarewell',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Invitation.helloGoodbyeInvite'
        db.add_column(u'rsvp_invitation', 'helloGoodbyeInvite',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Person.attending'
        db.add_column(u'rsvp_person', 'attending',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Person.attendingWedding'
        db.delete_column(u'rsvp_person', 'attendingWedding')

        # Deleting field 'Person.attendingWelcome'
        db.delete_column(u'rsvp_person', 'attendingWelcome')

        # Deleting field 'Person.attendingFarewell'
        db.delete_column(u'rsvp_person', 'attendingFarewell')

        # Deleting field 'Invitation.helloGoodbyeInvite'
        db.delete_column(u'rsvp_invitation', 'helloGoodbyeInvite')


    models = {
        u'rsvp.invitation': {
            'Meta': {'object_name': 'Invitation'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            'helloGoodbyeInvite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'plusOne': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'responded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'song': ('django.db.models.fields.TextField', [], {'max_length': '200', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'rsvp.person': {
            'Meta': {'object_name': 'Person'},
            'attendingFarewell': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'attendingWedding': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'attendingWelcome': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invitation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'people'", 'to': u"orm['rsvp.Invitation']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rsvp']
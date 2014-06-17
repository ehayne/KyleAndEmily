# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Invitation'
        db.create_table(u'rsvp_invitation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('responded', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'rsvp', ['Invitation'])

        # Adding model 'Person'
        db.create_table(u'rsvp_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invitation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='people', to=orm['rsvp.Invitation'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('attending', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('dietary_restrictions', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'rsvp', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Invitation'
        db.delete_table(u'rsvp_invitation')

        # Deleting model 'Person'
        db.delete_table(u'rsvp_person')


    models = {
        u'rsvp.invitation': {
            'Meta': {'object_name': 'Invitation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'responded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'rsvp.person': {
            'Meta': {'object_name': 'Person'},
            'attending': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'dietary_restrictions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invitation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'people'", 'to': u"orm['rsvp.Invitation']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rsvp']
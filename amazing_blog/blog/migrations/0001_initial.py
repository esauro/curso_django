# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'blog_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('intro', self.gf('django.db.models.fields.TextField')()),
            ('mas', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'blog', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'blog_post')


    models = {
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {}),
            'mas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blog']
# -*- coding: utf-8 -*-
import re
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    depends_on = (
        ('main', '0038_add_depends_optional_description.py'),
    )

    def forwards(self, orm):
        Depend = orm['packages.Depend']
        vcmp_re = re.compile(r"^(>=|<=|=|>|<)(.*)$")
        for old in orm['main.PackageDepend'].objects.all():
            comp = ver = ''
            m = vcmp_re.match(old.depvcmp)
            if m:
                comp = m.group(1)
                ver = m.group(2)
            new_dep = Depend(pkg_id=old.pkg_id, name=old.depname,
                    comparison=comp, version=ver, optional=old.optional,
                    description=old.description)
            new_dep.save(force_insert=True)

    def backwards(self, orm):
        orm['packages.Depend'].objects.all().delete()

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.arch': {
            'Meta': {'ordering': "['name']", 'object_name': 'Arch', 'db_table': "'arches'"},
            'agnostic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'main.donor': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Donor', 'db_table': "'donors'"},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'main.package': {
            'Meta': {'ordering': "('pkgname',)", 'unique_together': "(('pkgname', 'repo', 'arch'),)", 'object_name': 'Package', 'db_table': "'packages'"},
            'arch': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'packages'", 'on_delete': 'models.PROTECT', 'to': "orm['main.Arch']"}),
            'build_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'compressed_size': ('main.fields.PositiveBigIntegerField', [], {}),
            'epoch': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'files_last_update': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'flag_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'installed_size': ('main.fields.PositiveBigIntegerField', [], {}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'packager': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'packager_str': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pgp_signature': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pkgbase': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'pkgdesc': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'pkgname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pkgrel': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pkgver': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'repo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'packages'", 'on_delete': 'models.PROTECT', 'to': "orm['main.Repo']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'main.packagedepend': {
            'Meta': {'object_name': 'PackageDepend', 'db_table': "'package_depends'"},
            'depname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'depvcmp': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'optional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pkg': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'depends'", 'to': "orm['main.Package']"})
        },
        'main.packagefile': {
            'Meta': {'object_name': 'PackageFile', 'db_table': "'package_files'"},
            'directory': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_directory': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pkg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Package']"})
        },
        'main.repo': {
            'Meta': {'ordering': "['name']", 'object_name': 'Repo', 'db_table': "'repos'"},
            'bugs_category': ('django.db.models.fields.SmallIntegerField', [], {'default': '2'}),
            'bugs_project': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'staging': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'svn_root': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'testing': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'main.todolist': {
            'Meta': {'object_name': 'Todolist', 'db_table': "'todolists'"},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'on_delete': 'models.PROTECT'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'main.todolistpkg': {
            'Meta': {'unique_together': "(('list', 'pkg'),)", 'object_name': 'TodolistPkg', 'db_table': "'todolist_pkgs'"},
            'complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Todolist']"}),
            'pkg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Package']"})
        },
        'packages.conflict': {
            'Meta': {'ordering': "['name']", 'object_name': 'Conflict'},
            'comparison': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'pkg': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'conflicts'", 'to': "orm['main.Package']"}),
            'version': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'packages.depend': {
            'Meta': {'ordering': "['name']", 'object_name': 'Depend'},
            'comparison': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'optional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pkg': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'depends_new'", 'to': "orm['main.Package']"}),
            'version': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'packages.flagrequest': {
            'Meta': {'object_name': 'FlagRequest'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'is_legitimate': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_spam': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'num_packages': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'pkgbase': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'repo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Repo']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'user_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'packages.license': {
            'Meta': {'ordering': "['name']", 'object_name': 'License'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pkg': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'licenses'", 'to': "orm['main.Package']"})
        },
        'packages.packagegroup': {
            'Meta': {'object_name': 'PackageGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'pkg': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groups'", 'to': "orm['main.Package']"})
        },
        'packages.packagerelation': {
            'Meta': {'unique_together': "(('pkgbase', 'user', 'type'),)", 'object_name': 'PackageRelation'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pkgbase': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'package_relations'", 'to': "orm['auth.User']"})
        },
        'packages.provision': {
            'Meta': {'ordering': "['name']", 'object_name': 'Provision'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'pkg': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'provides'", 'to': "orm['main.Package']"}),
            'version': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'packages.replacement': {
            'Meta': {'ordering': "['name']", 'object_name': 'Replacement'},
            'comparison': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'pkg': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'replaces'", 'to': "orm['main.Package']"}),
            'version': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'packages.signoff': {
            'Meta': {'object_name': 'Signoff'},
            'arch': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Arch']"}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'epoch': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pkgbase': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'pkgrel': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pkgver': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'repo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Repo']"}),
            'revoked': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'package_signoffs'", 'to': "orm['auth.User']"})
        },
        'packages.signoffspecification': {
            'Meta': {'object_name': 'SignoffSpecification'},
            'arch': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Arch']"}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'epoch': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'known_bad': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pkgbase': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'pkgrel': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pkgver': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'repo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Repo']"}),
            'required': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        }
    }

    complete_apps = ['main', 'packages']
    symmetrical = True

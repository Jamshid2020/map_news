# Generated by Django 3.1.3 on 2020-12-03 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""CREATE OR REPLACE FUNCTION news_to_vector() RETURNS trigger AS $$
        begin
          new.document_vector := to_tsvector(new.content);
          return new;
        end
        $$ LANGUAGE plpgsql;"""),

        migrations.RunSQL("""CREATE TRIGGER news_update_vector BEFORE INSERT OR UPDATE
        ON maps_news FOR EACH ROW EXECUTE PROCEDURE news_to_vector();""")

    ]

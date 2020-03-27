#!/bin/bash

source ./backup_quack_db.config

echo "Start"
pg_dump -U $DB_USER -h localhost $DB_NAME > $BACKUP_DIR/$DB_NAME/$DATE-backup.sql
echo "Backup is done"

cd ./$BACKUP_DIR/$DB_NAME
BACKUPS_NUM=`find . -maxdepth 1 -type f | grep "backup" | wc -l`

if [ $BACKUPS_NUM -gt $MAX_BACKUPS_NUM ]
then
  echo "Started deleting old backups"
  EXCESS_BACKUPS_NUM=$(( $BACKUPS_NUM - $MAX_BACKUPS_NUM ))
  for (( i==1; i<$EXCESS_BACKUPS_NUM; i++ ))
  do
  rm ./$(ls | grep "backup" | sort | head -n 1)
  done
  echo "Deleting is done"
fi

cd donnee
echo effacement des fichiers csv
rm *.csv
echo effacement des fichiers xlsx
rm *.xlsx
echo 'telechargement des données'
curl -X GET 'https://data.ameli.fr/api/explore/v2.1/catalog/datasets/effectifs/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B' >> effectifs.csv
curl -X GET 'https://data.ameli.fr/api/explore/v2.1/catalog/datasets/depenses/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B'  >> depenses.csv
curl -X GET 'https://www.insee.fr/fr/outil-interactif/5014911/data/FR/donnees_pyramide_act.csv'  >> pop.csv
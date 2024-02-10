UPDATE VETEMENTS_ANTENNE
SET ma_colonne = 
    REPLACE(
        REPLACE(
            REPLACE(
                REPLACE(
                    REPLACE(
                        REPLACE(
                            REPLACE(
                                REPLACE(
                                    REPLACE(
                                        REPLACE(
                                            REPLACE(
                                                REPLACE(
                                                    REPLACE(
                                                        REPLACE(
                                                            REPLACE(
                                                                REPLACE(
                                                                    REPLACE(
                                                                        REPLACE(
                                                                            REPLACE(
                                                                                REPLACE(
                                                                                    REPLACE(
                                                                                        REPLACE(
                                                                                            REPLACE(
                                                                                                REPLACE(
                                                                                                    ma_colonne,
                                                                                                    'à', 'a'
                                                                                                ),
                                                                                                'â', 'a'
                                                                                            ),
                                                                                            'ä', 'a'
                                                                                        ),
                                                                                        'ç', 'c'
                                                                                    ),
                                                                                    'è', 'e'
                                                                                ),
                                                                                'é', 'e'
                                                                            ),
                                                                            'ê', 'e'
                                                                        ),
                                                                        'ë', 'e'
                                                                    ),
                                                                    'î', 'i'
                                                                ),
                                                                'ï', 'i'
                                                            ),
                                                            'ô', 'o'
                                                        ),
                                                        'ö', 'o'
                                                    ),
                                                    'ù', 'u'
                                                ),
                                                'û', 'u'
                                            ),
                                            'ü', 'u'
                                        ),
                                        'À', 'A'
                                    ),
                                    'Â', 'A'
                                ),
                                'Ä', 'A'
                            ),
                            'Ç', 'C'
                        ),
                        'È', 'E'
                    ),
                    'É', 'E'
                ),
                'Ê', 'E'
            ),
            'Ë', 'E'
        ),
        'Î', 'I'
    );

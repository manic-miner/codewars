def human_years_cat_years_dog_years(human_years):
    cat_years = 24 + 4 * (human_years - 2) if human_years > 1 else 15
    dog_years = 24 + 5 * (human_years - 2) if human_years > 1 else 15

    return [human_years, cat_years, dog_years]
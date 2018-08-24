
msp = MimicServerPlatform.ctor0("postgres", "public")
msp.connect()

echo = EchoKit.Echo (interface = msp)

cohort = CohortBuilder.MomentCohortBuilder(agent = echo, allow_patient_duplication = True)

# Inclusion Criteria

extubation_event_filter = FilterCollection.extubation()  # Anonymous Function (Lambda)
age_filter = Filter.NumericFilter( target = CONST.AGE, operater = '>=', value = '15')



# Exclusion Criteria

potential_comfort_care_filter = FilterCollection.comfortcareFilter()

cohort.set_inclusion_filters([extubation_event_filter, age_filter])
cohort.set_exclusion_filters([potential_comfort_care_filter])
cohort.set_maximum_subject_number(100)
cohort.build()


target = cohort.get_by_index(0)
print( target )

# same

target = cohort.set_index(0)
print (target)
print (cohort.currentTarget())

target = cohort.next()
print( target )
print (cohort.currentIndex)


# Working on the first patient

target = cohort.get_by_index (0)

# Let's talk about this patient... on 7/10 9am
echo.set_focus (target)

extubation_status = echo.gatherer.getExtubationStatus()

rsbi =  extubation_status.get_data('recent_respiratory_rate') / extubation_status.get_data('recent_tidal_volume')
is_dead_during_hospitalizatin = echo.ask.if_dead_during_hospitalization()



reintubation_status = echo.gatherer.getReintubationStatus( hour = 48 )

is_reintubated = reintubation_status.get_data('if_reintubated')




#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""

import argparse

from inflammation import models, views,classes


def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    in_files = args.infiles
    if not isinstance(in_files, list):
        in_files = [args.infiles]

    for filename in in_files:
        inflammation_data = models.load_csv(filename)

        if args.view == "visualise":
            view_data = {
                'average': models.daily_mean(inflammation_data), 
                'standard_deviation': models.daily_stdev(inflammation_data), 
                'max': models.daily_max(inflammation_data), 
                'min': models.daily_min(inflammation_data)
                }

            views.visualize(view_data)
        elif args.view == 'record':
            patient_data = inflammation_data[args.patient]
            observations = [classes.Observation(day,value) for day,value in enumerate(patient_data)]
            patient = classes.Patient('UNKNOWN',observations)


            views.display_patient_record(patient)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic patient inflammation data management system')

    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing inflammation series for each patient')

    parser.add_argument(
        '--view',
        default='visualise',
        choices = ['visualise','record'],
        help='Which view should be used?')

    parser.add_argument(
        '--patient',
        type=int,
        default=0,
        help='Which patient should be displayed?')

    args = parser.parse_args()

    main(args)

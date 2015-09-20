#!/usr/bin/env python

# Take any number of command line args and create
# a Morea module folder and files, filled with
# TODOs

import sys
import os
import argparse
from src.module import make_module
from src.outcome import make_outcome
from src.reading import make_reading
from src.experience import make_experience
from src.assessment import make_assessment

def main():
    parser = argparse.ArgumentParser(
    epilog="""
    Docs at http://genomeannotation.github.io/GAG/
    Bugs and feature requests at https://github.com/genomeannotation/GAG/issues
    """,
    formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('-t', '--title', required=True)
    parser.add_argument('-o', '--order', required=True)
    parser.add_argument('-i', '--icon')
    parser.add_argument('-o1t', '--outcome-one-title')
    parser.add_argument('-o2t', '--outcome-two-title')
    parser.add_argument('-r1t', '--reading-one-title')
    parser.add_argument('-r2t', '--reading-two-title')
    parser.add_argument('-r1s', '--reading-one-summary')
    parser.add_argument('-r2s', '--reading-two-summary')
    parser.add_argument('-r1u', '--reading-one-url')
    parser.add_argument('-r2u', '--reading-two-url')
    parser.add_argument('-e1t', '--experience-one-title')
    parser.add_argument('-e2t', '--experience-two-title')
    parser.add_argument('-e1s', '--experience-one-summary')
    parser.add_argument('-e2s', '--experience-two-summary')
    parser.add_argument('-a1t', '--assessment-one-title')
    parser.add_argument('-a2t', '--assessment-two-title')
    args = parser.parse_args()
    module_title = args.title.replace(" ", "_")

    # Make folder
    folder_name = str(args.order) + "." + module_title
    os.mkdir(folder_name)

    # Navigate into that folder
    os.chdir(folder_name)

    # Write module file
    with open("module.md", "w") as modfile:
        module_contents = make_module(module_title, args.order, args.icon)
        modfile.write(module_contents)

    # Write outcome files
    with open("outcome-1.md", "w") as outcome1:
        outcome_contents = make_outcome(module_title, args.outcome_one_title, 1)
        outcome1.write(outcome_contents)
    with open("outcome-2.md", "w") as outcome2:
        outcome_contents = make_outcome(module_title, args.outcome_two_title, 2)
        outcome2.write(outcome_contents)

    # Write reading files
    with open("reading-1.md", "w") as reading1:
        reading_contents = make_reading(module_title, args.reading_one_title,
                args.reading_one_summary, args.reading_one_url, 1)
        reading1.write(reading_contents)
    with open("reading-2.md", "w") as reading2:
        reading_contents = make_reading(module_title, args.reading_two_title,
                args.reading_two_summary, args.reading_two_url, 2)
        reading2.write(reading_contents)

    # Write experience files
    with open("experience-1.md", "w") as experience1:
        experience_contents = make_experience(module_title, args.experience_one_title,
                args.experience_one_summary, 1)
        experience1.write(experience_contents)
    with open("experience-2.md", "w") as experience2:
        experience_contents = make_experience(module_title, args.experience_two_title,
                args.experience_two_summary, 2)
        experience2.write(experience_contents)

    # Write assessment files
    with open("assessment-1.md", "w") as assessment1:
        assessment_contents = make_assessment(module_title, args.assessment_one_title, 1)
        assessment1.write(assessment_contents)
    with open("assessment-2.md", "w") as assessment2:
        assessment_contents = make_assessment(module_title, args.assessment_two_title, 2)
        assessment2.write(assessment_contents)


##########################

if __name__ == '__main__':
    main()

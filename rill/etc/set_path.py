from abjad import *
import rill
import os
import importlib
import shutil

score_package_path = rill.__path__[0]
segments_package_path = os.path.join(score_package_path, 'segments')
segment_names = [
        name for name in
        os.listdir(segments_package_path)
        if os.path.isdir(os.path.join(segments_package_path, name)) and
        not name.startswith(('.', '_'))
    ]

#segment_names
#['segment_a_far_sorr', 'segment_b_selidor_a', 'segment_c_wellogy', 
#'segment_d_the_long_dune_a', 'segment_e_selidor_b', 
#'segment_f_the_isle_of_the_ear', 'segment_g_selidor_c', 
#'segment_h_the_long_dune_b']


segment_definition_modules = []
for segment_name in segment_names:
    path_parts = ['rill', 'segments', segment_name, 'definition']
    package_path = '.'.join(path_parts)
    definition_module = importlib.import_module(package_path)
    segment_definition_modules.append(definition_module)


for segment_definition_module in segment_definition_modules:
    segment_directory = os.path.dirname(segment_definition_module.__file__)
    pdf_path = os.path.join(segment_directory, 'illustration.pdf')
    segment_maker = segment_definition_module.segment_maker
    persist(segment_maker).as_pdf(pdf_path)

score_path = rill.__path__[0]
segments_path = os.path.join(score_path, 'segments')
build_segments_path = os.path.join(score_path, 'build', 'segments')
for segment_name in os.listdir(segments_path):
    # First, check that we have found an actual segment subpackage.
    if segment_name.startswith(('.', '_')):  # Skip hidden files.
        continue
    segment_path = os.path.join(segments_path, segment_name)
    if not os.path.isdir(segment_path):  # Skip if not a subdirectory.
        continue
    # Import the segment definition.
    definition_module_pieces = ['rill', 'segments', segment_name, 'definition']
    definition_module_path = '.'.join(definition_module_pieces)
    definition_module = importlib.import_module(definition_module_path)
    # Illustrate the segment definition inside its segment package.
    segment_maker = definition_module.segment_maker
    pdf_path = os.path.join(segment_path, 'illustration.pdf')
    persist(segment_maker).as_pdf(pdf_path)  # Also creates illustration.ly
    # Copy the segment's LilyPond file into the build/ directory.
    ly_source_path = os.path.join(segment_path, 'illustration.ly')
    ly_target_name = '{}.ly'.format(segment_name.replace('_', '-'))
    ly_target_path = os.path.join(build_segments_path, ly_target_name)
    shutil.copy(ly_source_path, ly_target_path)

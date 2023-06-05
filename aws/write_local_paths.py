import os
import argparse


def write_local_paths(root_dir, output_file):
    # Store all file paths
    nii_files = []
    mask_files = []

    # Walk through the directory
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            # Check if it's a .nii.gz file
            if filename.endswith('.nii.gz') and not filename.endswith('BrainMask.nii.gz'):
                nii_files.append(os.path.abspath(os.path.join(dirpath, filename)))
            # Check if it's a mask file
            if filename.endswith('BrainMask.nii.gz'):
                mask_files.append(os.path.abspath(os.path.join(dirpath, filename)))

    # Write the file paths to the output file
    with open(output_file, 'w') as f:
        for nii, mask in zip(nii_files, mask_files):
            f.write(f'{nii},{mask}\n')


def main():
    parser = argparse.ArgumentParser(description='Write local paths to nifti and mask files.')
    parser.add_argument('-d', '--directory', help='Path to the root directory.', required=True)
    parser.add_argument('-o', '--output', help='Path to the output text file.', required=True)
    args = parser.parse_args()

    write_local_paths(args.directory, args.output)


if __name__ == '__main__':
    main()
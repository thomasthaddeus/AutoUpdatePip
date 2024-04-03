#  main.py

from .pip_batch_update import batcher, get_outdated_packages, update_packages, setup_logging

def main():
    """
    The main execution function of the script.

    Sets up logging, identifies and updates outdated pip packages in batches,
    and then displays the difference in outdated packages before and after the
    update.
    """
    setup_logging()

    initial_outdated = get_outdated_packages()

    # Update packages in batches of 10 using the recursive batcher
    for batch in batcher(initial_outdated, 10):
        update_packages(batch)

    final_outdated = get_outdated_packages()

    # Find the difference
    still_outdated = set(final_outdated) - set(initial_outdated)
    newly_updated = set(initial_outdated) - set(final_outdated)

    print("Still Outdated:")
    for package in still_outdated:
        print(package)

    print("\nNewly Updated:")
    for package in newly_updated:
        print(package)


if __name__ == "__main__":
    main()

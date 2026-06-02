import argparse
import fnmatch
import unittest


def iter_tests(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from iter_tests(item)
        else:
            yield item


def build_suite(start="tests/unit", pattern="*_spec.py", top=".", k=None):
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=start, pattern=pattern, top_level_dir=top)

    if not k:
        return suite

    filtered = unittest.TestSuite()
    for test in iter_tests(suite):
        test_name = test.id()
        if fnmatch.fnmatchcase(test_name, k) or k in test_name:
            filtered.addTest(test)

    return filtered


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start", default="tests/unit")
    parser.add_argument("-p", "--pattern", default="*_spec.py")
    parser.add_argument("-t", "--top", default=".")
    parser.add_argument("-k", default=None)
    parser.add_argument("-v", "--verbose", action="count", default=0)
    args = parser.parse_args(argv)

    suite = build_suite(start=args.start, pattern=args.pattern, top=args.top, k=args.k)
    runner = unittest.TextTestRunner(verbosity=1 + args.verbose)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())

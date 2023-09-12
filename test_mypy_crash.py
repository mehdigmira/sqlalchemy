import tempfile
from mypy import api

with tempfile.TemporaryDirectory() as cachedir:
    for path in (
        # "test/typing/plain_files/ext/association_proxy/association_proxy_one.py",
        # "test/typing/plain_files/ext/association_proxy/association_proxy_three.py",
        "test/typing/plain_files/ext/association_proxy/association_proxy_two.py",
        "test/typing/plain_files/ext/asyncio/async_sessionmaker.py",
    ):
        args = [
            # "--no-incremental",
            "--enable-incomplete-feature=TypeVarTuple",
            "--enable-incomplete-feature=Unpack",
            "--strict",
            "--raise-exceptions",
            "--cache-dir",
            cachedir,
            "--config-file",
            "plain_mypy.ini",
        ]

        # mypy as of 0.990 is more aggressively blocking messaging
        # for paths that are in sys.path, and as pytest puts currdir,
        # test/ etc in sys.path, just copy the source file to the
        # tempdir we are working in so that we don't have to try to
        # manipulate sys.path and/or guess what mypy is doing
        # filename = os.path.basename(path)
        # test_program = os.path.join(use_cachedir, filename)
        # if path != test_program:
        #     shutil.copyfile(path, test_program)
        args.append(path)
        api.run(args)

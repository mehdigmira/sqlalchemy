import os

from sqlalchemy import testing
from sqlalchemy.testing import fixtures


class MypyPlainTest(fixtures.MypyTest):
    @testing.combinations(
        *(
            (os.path.basename(path), path)
            for path in fixtures.MypyTest.file_combinations("plain_files")
        ),
        argnames="path",
        id_="ia",
    )
    def test_mypy_no_plugin(self, mypy_typecheck_file, path):
        mypy_typecheck_file(path)


class MypyPlainTest2(fixtures.MypyTest):
    def test_mypy_no_plugin_0(self, mypy_typecheck_file):
        mypy_typecheck_file(
            "/code/.debug/sqlalchemy/test/typing/plain_files/ext/association_proxy/association_proxy_one.py"
        )

    def test_mypy_no_plugin_1(self, mypy_typecheck_file):
        mypy_typecheck_file(
            "/code/.debug/sqlalchemy/test/typing/plain_files/ext/association_proxy/association_proxy_three.py"
        )

    def test_mypy_no_plugin_2(self, mypy_typecheck_file):
        mypy_typecheck_file(
            "/code/.debug/sqlalchemy/test/typing/plain_files/ext/association_proxy/association_proxy_two.py"
        )

    def test_mypy_no_plugin_3(self, mypy_typecheck_file):
        mypy_typecheck_file(
            "/code/.debug/sqlalchemy/test/typing/plain_files/ext/asyncio/async_sessionmaker.py"
        )

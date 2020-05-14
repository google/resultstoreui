workspace(name = "com_google_resultstore")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# Python rules should go early in the dependencies list, otherwise a wrong
# version of the library will be selected as a transitive dependency of gRPC.
http_archive(
    name = "rules_python",
    url = "https://github.com/bazelbuild/rules_python/archive/748aa53d7701e71101dfd15d800e100f6ff8e5d1.zip",
    strip_prefix = "rules_python-748aa53d7701e71101dfd15d800e100f6ff8e5d1"
)

load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()

load("@rules_python//python:pip.bzl", "pip_repositories")
pip_repositories()

load("@rules_python//python:pip.bzl", "pip3_import")

pip3_import(   # or pip3_import
   name = "grpc_deps",
   requirements = "//:requirements.txt",
)

# Load the central repo's install function from its `//:requirements.bzl` file,
# and call it.
load("@grpc_deps//:requirements.bzl", "pip_install")
pip_install()

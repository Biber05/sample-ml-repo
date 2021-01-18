import os
from typing import Union, Dict

from ccmlutils.config.envconfig import RUN_ID_KEY, SHORT_ID_KEY, get_and_ask_for_exp_name
from ccmlutils.utilities.hashutils import generate_short_id
from ccmlutils.utilities.timeutils import generate_timestamp
from kedro.framework.context import KedroContext
from kedro.pipeline import Pipeline

from src.mltemplate.pipeline import create_pipelines


class ProjectContext(KedroContext):
    """Users can override the remaining methods from the parent class here,
    or create new ones (e.g. as required by plugins)
    """

    def _get_save_version(self):
        # This is a version where no UTC is given in order to support other regions
        return generate_timestamp()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._local_run_id = self._get_save_version()
        self._local_short_id = generate_short_id(self._local_run_id)
        os.environ[RUN_ID_KEY] = self._local_run_id
        os.environ[SHORT_ID_KEY] = self._local_short_id
        exp_name, should_commit = get_and_ask_for_exp_name()
        exp_name = exp_name if len(exp_name) > 0 else "DEBUG-EXPERIMENT"
        print(f"Init Context with: {exp_name} ; {should_commit}")
        if should_commit:
            pass
            # todo
            # fast_commit(["/conf/base", "mltemplate"], "EXP-COMMIT: " + exp_name)

    project_name = "mltemplate"
    # Here the kedro sample version is used
    project_version = "0.17.0"

    def _get_run_id(
            self, *args, **kwargs  # pylint: disable=unused-argument
    ) -> Union[None, str]:
        return self._local_run_id

    def _get_pipelines(self) -> Dict[str, Pipeline]:
        return create_pipelines()

# Copyright 2020 The Tekton Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Tekton

    Tekton Pipeline  # noqa: E501

    The version of the OpenAPI document: v0.17.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import tekton_pipeline
from tekton_pipeline.models.v1beta1_internal_task_modifier import V1beta1InternalTaskModifier  # noqa: E501
from tekton_pipeline.rest import ApiException

class TestV1beta1InternalTaskModifier(unittest.TestCase):
    """V1beta1InternalTaskModifier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1InternalTaskModifier
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tekton_pipeline.models.v1beta1_internal_task_modifier.V1beta1InternalTaskModifier()  # noqa: E501
        if include_optional :
            return V1beta1InternalTaskModifier(
                steps_to_append = [
                    tekton_pipeline.models.v1beta1/step.v1beta1.Step(
                        args = [
                            '0'
                            ], 
                        command = [
                            '0'
                            ], 
                        env = [
                            None
                            ], 
                        env_from = [
                            None
                            ], 
                        image = '0', 
                        image_pull_policy = '0', 
                        lifecycle = None, 
                        liveness_probe = None, 
                        name = '0', 
                        ports = [
                            None
                            ], 
                        readiness_probe = None, 
                        resources = None, 
                        script = '0', 
                        security_context = None, 
                        startup_probe = None, 
                        stdin = True, 
                        stdin_once = True, 
                        termination_message_path = '0', 
                        termination_message_policy = '0', 
                        timeout = None, 
                        tty = True, 
                        volume_devices = [
                            None
                            ], 
                        volume_mounts = [
                            None
                            ], 
                        working_dir = '0', )
                    ], 
                steps_to_prepend = [
                    tekton_pipeline.models.v1beta1/step.v1beta1.Step(
                        args = [
                            '0'
                            ], 
                        command = [
                            '0'
                            ], 
                        env = [
                            None
                            ], 
                        env_from = [
                            None
                            ], 
                        image = '0', 
                        image_pull_policy = '0', 
                        lifecycle = None, 
                        liveness_probe = None, 
                        name = '0', 
                        ports = [
                            None
                            ], 
                        readiness_probe = None, 
                        resources = None, 
                        script = '0', 
                        security_context = None, 
                        startup_probe = None, 
                        stdin = True, 
                        stdin_once = True, 
                        termination_message_path = '0', 
                        termination_message_policy = '0', 
                        timeout = None, 
                        tty = True, 
                        volume_devices = [
                            None
                            ], 
                        volume_mounts = [
                            None
                            ], 
                        working_dir = '0', )
                    ], 
                volumes = [
                    None
                    ]
            )
        else :
            return V1beta1InternalTaskModifier(
                steps_to_append = [
                    tekton_pipeline.models.v1beta1/step.v1beta1.Step(
                        args = [
                            '0'
                            ], 
                        command = [
                            '0'
                            ], 
                        env = [
                            None
                            ], 
                        env_from = [
                            None
                            ], 
                        image = '0', 
                        image_pull_policy = '0', 
                        lifecycle = None, 
                        liveness_probe = None, 
                        name = '0', 
                        ports = [
                            None
                            ], 
                        readiness_probe = None, 
                        resources = None, 
                        script = '0', 
                        security_context = None, 
                        startup_probe = None, 
                        stdin = True, 
                        stdin_once = True, 
                        termination_message_path = '0', 
                        termination_message_policy = '0', 
                        timeout = None, 
                        tty = True, 
                        volume_devices = [
                            None
                            ], 
                        volume_mounts = [
                            None
                            ], 
                        working_dir = '0', )
                    ],
                steps_to_prepend = [
                    tekton_pipeline.models.v1beta1/step.v1beta1.Step(
                        args = [
                            '0'
                            ], 
                        command = [
                            '0'
                            ], 
                        env = [
                            None
                            ], 
                        env_from = [
                            None
                            ], 
                        image = '0', 
                        image_pull_policy = '0', 
                        lifecycle = None, 
                        liveness_probe = None, 
                        name = '0', 
                        ports = [
                            None
                            ], 
                        readiness_probe = None, 
                        resources = None, 
                        script = '0', 
                        security_context = None, 
                        startup_probe = None, 
                        stdin = True, 
                        stdin_once = True, 
                        termination_message_path = '0', 
                        termination_message_policy = '0', 
                        timeout = None, 
                        tty = True, 
                        volume_devices = [
                            None
                            ], 
                        volume_mounts = [
                            None
                            ], 
                        working_dir = '0', )
                    ],
                volumes = [
                    None
                    ],
        )

    def testV1beta1InternalTaskModifier(self):
        """Test V1beta1InternalTaskModifier"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
#
# OctoPrint Filament_Change plugin.
#
# Copyright (c) 2023,2025 Pete Turnbull <pete@dunnington.cx>
# Original Copyright (c) 2019, Jim Pingle <jim@pingle.org>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import absolute_import

import octoprint.plugin

class filamentchangePlugin(octoprint.plugin.SettingsPlugin,
				octoprint.plugin.AssetPlugin,
				octoprint.plugin.TemplatePlugin):

	def get_settings_defaults(self):
		return dict(
			unload_length=450,
			unload_speed=1600,
			load_length=420,
			load_speed=800,
			purge_length=25,
			purge_speed=240,
			pause_before_park=False,
			retract_before_park=True,
			retract_length=5,
			retract_speed=240,
			home_before_park=False,
			y_park=0,
			x_park=0,
			z_lift_relative=20,
			park_speed=4200
		)

	def get_template_configs(self):
		return [dict(type="settings", custom_bindings=False)]

	def get_assets(self):
		return dict(
			js=["js/FilamentChange.js"],
			css=["css/FilamentChange.css"]
		)

	def get_update_information(self):
		return dict(
			Filament_Change=dict(
				displayName="Filament Change",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="pnt103",
				repo="OctoPrint-FilamentChange",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/pnt103/OctoPrint-FilamentChange/archive/{target_version}.zip"
			)
		)


__plugin_name__ = "Filament Change"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = filamentchangePlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}


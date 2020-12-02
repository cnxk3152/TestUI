# -*- coding:utf-8 -*-

from airtest.cli.runner import AirtestCase, run_script
import airtest.report.report as report
from conf.settings import *
from argparse import *
import shutil, os, io, jinja2, datetime


class Air_Case_Handler(AirtestCase):
    def setUp(self):
        super(Air_Case_Handler, self).setUp()

    def tearDown(self):
        super(Air_Case_Handler, self).tearDown()

    def run_air(self, air_dir, device):
        start_time = datetime.datetime.now()
        start_time_fmt = start_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        results = []
        root_log = log_path
        if os.path.isdir(root_log):
            shutil.rmtree(root_log)
        else:
            os.makedirs(root_log)

        for file in os.listdir(air_path):
            if file.endswith(".air"):
                airName = file
                airDirName = file.replace(".air", "")
                script = os.path.join(air_dir, file)
                air_log = os.path.join(root_path, "log\\" + airDirName)
                if os.path.isdir(air_log):
                    # print(air_log)
                    shutil.rmtree(air_log)
                else:
                    os.makedirs(air_log)

                html = os.path.join(air_log, "log.html")
                args = Namespace(device=device, log=air_log, recording=None, script=script)
                try:
                    run_script(args, AirtestCase)
                except AssertionError as e:
                    pass
                finally:
                    rpt = report.LogToHtml(script, air_log)
                    rpt.report("log_template.html", output_file=html)
                    result = {}
                    result["name"] = airName.replace('.air', '')
                    result["result"] = rpt.test_result
                    results.append(result)

        end_time = datetime.datetime.now()
        end_time_fmt = end_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        duration = (end_time - start_time).seconds
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_path),
            extensions=(),
            autoescape=True
        )

        template = env.get_template(template_name, template_path)
        project_name = root_path.split("\\")[-1]
        success = 0
        fail = 0
        for res in results:
            if res['result']:
                success += 1
            else:
                fail += 1
        report_name = "report_" + end_time.strftime("%Y%m%d%H%M%S") + ".html"
        html = template.render(
            {"results": results, "stime": start_time_fmt, 'etime': end_time_fmt, 'duration': duration,
             "project": project_name, "success": success, "fail": fail})
        output_file = os.path.join(root_path, "report", report_name)
        with io.open(output_file, 'w', encoding="utf-8") as f:
            f.write(html)


if __name__ == "__main__":
    test = Air_Case_Handler()
    test.run_air(air_path, devices)

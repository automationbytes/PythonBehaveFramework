from behave import __main__ as runner
import sys
import os

if __name__ == '__main__':
    sys.stdout.flush()

    FeatureFilePath = 'FeaturesFiles'
    Tags = ' --tags=Regression '
    AllureReportPath = ' -f allure_behave.formatter:AllureFormatter -o reporting-folder'
    behaveOptions = ' --summary --capture --capture-stderr -f plain'
    reportdir = os.getcwd()+"\\reporting-folder"
    run = FeatureFilePath+Tags+AllureReportPath+behaveOptions
    runner.main(run)

    os.system('cmd /c "allure serve "'+reportdir)

    #Tags = ' --tags=Sanity ' - only sanity
    #Tags = ' --tags=-Sanity ' - expect sanity
    #Tags = ' --tags=Sanity,Regression ' OR
    #Tags = ' --tags=Sanity --tags=Regression ' AND




"""
A module for obtaining repo readme and language data from the github API.
Before using this module, read through it, and follow the instructions marked
TODO.
After doing so, run it like this:
    python acquire.py
To create the `data.json` file that contains the data.
"""
import os
import json
from typing import Dict, List, Optional, Union, cast
import requests

from env import github_token, github_username

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token https://github.com/settings/tokens
#        You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Add your github username to your env.py file under the variable `github_username`
# TODO: Add more repositories to the `REPOS` list below.

REPOS = ['jtleek/datasharing',
 'rdpeng/ProgrammingAssignment2',
 'octocat/Spoon-Knife',
 'tensorflow/tensorflow',
 'SmartThingsCommunity/SmartThingsPublic',
 'twbs/bootstrap',
 'github/gitignore',
 'rdpeng/ExData_Plotting1',
 'tensorflow/models',
 'nightscout/cgm-remote-monitor',
 'facebook/react',
 'DataScienceSpecialization/courses',
 'angular/angular.js',
 'jlord/patchwork',
 'barryclark/jekyll-now',
 'Snailclimb/JavaGuide',
 'firstcontributions/first-contributions',
 'bitcoin/bitcoin',
 'spring-projects/spring-framework',
 'vuejs/vue',
 'getify/You-Dont-Know-JS',
 'freeCodeCamp/freeCodeCamp',
 'kubernetes/kubernetes',
 'mrdoob/three.js',
 'udacity/frontend-nanodegree-resume',
 'TheAlgorithms/Python',
 'LarryMad/recipes',
 'ant-design/ant-design',
 'd3/d3',
 'apache/spark',
 'DefinitelyTyped/DefinitelyTyped',
 'django/django',
 'apache/dubbo',
 '996icu/996.ICU',
 'justjavac/free-programming-books-zh_CN',
 'ohmyzsh/ohmyzsh',
 'scikit-learn/scikit-learn',
 'shadowsocks/shadowsocks',
 'facebook/react-native',
 'jquery/jquery',
 'PanJiaChen/vue-element-admin',
 'git/git',
 'ansible/ansible',
 'facebook/create-react-app',
 'slatedocs/slate',
 'airbnb/javascript',
 'dotnet/AspNetCore.Docs',
 'iluwatar/java-design-patterns',
 'laravel/laravel',
 'rails/rails',
 'BVLC/caffe',
 'keras-team/keras',
 'sindresorhus/awesome',
 'kamranahmedse/developer-roadmap',
 'donnemartin/system-design-primer',
 'nodejs/node',
 'antirez/redis',
 'elastic/elasticsearch',
 'angular/angular',
 'moby/moby',
 'mui-org/material-ui',
 'vinta/awesome-python',
 'gabrielecirulli/2048',
 'shadowsocks/shadowsocks-windows',
 'microsoft/vscode',
 'wakaleo/game-of-life',
 'macrozheng/mall',
 'wesbos/JavaScript30',
 'python/cpython',
 'hakimel/reveal.js',
 'helm/charts',
 'atom/atom',
 'ColorlibHQ/AdminLTE',
 'apache/incubator-echarts',
 'animate-css/animate.css',
 'xingshaocheng/architect-awesome',
 'udacity/course-collaboration-travel-plans',
 'aymericdamien/TensorFlow-Examples',
 'reduxjs/redux',
 'tastejs/todomvc',
 'CSSEGISandData/COVID-19',
 'pallets/flask',
 'ionic-team/ionic',
 'qmk/qmk_firmware',
 'flutter/flutter',
 'pjreddie/darknet',
 'odoo/odoo',
 'doocs/advanced-java',
 'Homebrew/legacy-homebrew',
 'selfteaching/the-craft-of-selfteaching',
 'trekhleb/javascript-algorithms',
 'jenkins-docs/simple-java-maven-app',
 'Trinea/android-open-project',
 'udacity/fullstack-nanodegree-vm',
 'scutan90/DeepLearning-500-questions',
 'danielmiessler/SecLists',
 'ytdl-org/youtube-dl',
 'josephmisiti/awesome-machine-learning',
 'protocolbuffers/protobuf',
 'netty/netty',
 'mmistakes/minimal-mistakes',
 'electron/electron',
 '233boy/v2ray',
 'shadowsocks/shadowsocks-android',
 'bailicangdu/vue2-elm',
 'h5bp/html5-boilerplate',
 'scm-ninja/starter-web',
 'ageron/handson-ml',
 'FortAwesome/Font-Awesome',
 'getlantern/lantern',
 'heroku/node-js-sample',
 'ElemeFE/element',
 'home-assistant/core',
 'golang/go',
 'Azure/azure-quickstart-templates',
 'chartjs/Chart.js',
 'jakevdp/PythonDataScienceHandbook',
 'pandas-dev/pandas',
 'android/architecture-samples',
 'MicrosoftDocs/azure-docs',
 'MisterBooo/LeetCodeAnimation',
 'ityouknow/spring-boot-examples',
 'rapid7/metasploit-framework',
 'udacity/create-your-own-adventure',
 'pytorch/pytorch',
 'AFNetworking/AFNetworking',
 'public-apis/public-apis',
 'wesm/pydata-book',
 'coolsnowwolf/lede',
 'PX4/Firmware',
 'MicrosoftDocs/mslearn-tailspin-spacegame-web',
 'MarlinFirmware/Marlin',
 'deepfakes/faceswap',
 'esp8266/Arduino',
 'ageitgey/face_recognition',
 'wasabeef/awesome-android-ui',
 'karan/Projects',
 'CoreyMSchafer/code_snippets',
 'astaxie/build-web-application-with-golang',
 'ethereum/go-ethereum',
 'googlehosts/hosts',
 'kdn251/interviews',
 'spring-projects/spring-petclinic',
 'ArduPilot/ardupilot',
 'mdn/learning-area',
 'linuxacademy/devops-essentials-sample-app',
 'TheAlgorithms/Java',
 'bettiolo/node-echo',
 'angular/angular-cli',
 'testerSunshine/12306',
 'socketio/socket.io',
 'google/styleguide',
 'mybatis/mybatis-3',
 'ossu/computer-science',
 'Blankj/AndroidUtilCode',
 'h5bp/Front-end-Developer-Interview-Questions',
 'jekyll/jekyll',
 'nolimits4web/swiper',
 'jlevy/the-art-of-command-line',
 'leereilly/swot',
 'apachecn/AiLearning',
 'zxing/zxing',
 'CocoaPods/Specs',
 'scrapy/scrapy',
 'WordPress/WordPress',
 'academicpages/academicpages.github.io',
 'AllenDowney/ThinkStats2',
 'vivienzou1/DL-Notes-for-Interview',
 'necolas/normalize.css',
 'apache/kafka',
 'adam-p/markdown-here',
 'google/guava',
 'apple/swift',
 'geekcomputers/Python',
 'georgearun/Data-Science--Cheat-Sheet',
 'exacity/deeplearningbook-chinese',
 'Homebrew/homebrew-cask',
 'daattali/beautiful-jekyll',
 'google/material-design-icons',
 'ServiceNow/devtraining-needit-madrid',
 'microsoft/TypeScript',
 'gatsbyjs/gatsby',
 'ReactTraining/react-router',
 'expressjs/express',
 'blueimp/jQuery-File-Upload',
 'matterport/Mask_RCNN',
 'learn-co-students/python-practice-with-datatypes-data-science-intro-000',
 'mathiasbynens/dotfiles',
 'lewagon/dotfiles',
 'PHPMailer/PHPMailer',
 'kelthuzadx/hosts',
 'square/okhttp',
 'hasura/imad-app',
 'jleetutorial/maven-project',
 'ruanyf/es6tutorial',
 'labuladong/fucking-algorithm',
 'vuejs/vuex',
 'Homebrew/homebrew-core',
 'PhilJay/MPAndroidChart',
 'geekcompany/ResumeSample',
 'fivethirtyeight/data',
 'XX-net/XX-Net',
 'bcit-ci/CodeIgniter',
 'psf/requests',
 'vuejs/awesome-vue',
 'nodejs/node-v0.x-archive',
 'kallaway/100-days-of-code',
 'symfony/symfony',
 'shadowsocks/ShadowsocksX-NG',
 'ctripcorp/apollo',
 'magento/magento2',
 'dmlc/xgboost',
 'chanjarster/weixin-java-tools',
 '0voice/interview_internal_reference',
 'vercel/next.js',
 'microsoft/Windows-universal-samples',
 'TryGhost/Ghost',
 'checkstyle/checkstyle',
 'swagger-api/swagger-ui',
 'laravel/framework',
 'v2ray/v2ray-core',
 'coding-boot-camp/prework-about-me',
 'learn-co-students/python-variables-readme-data-science-intro-000',
 'shuzheng/zheng',
 'ServiceNow/devtraining-needit-kingston',
 'angular/angular-seed',
 'kubernetes/website',
 'avelino/awesome-go',
 'Avik-Jain/100-Days-Of-ML-Code',
 'mozilla/pdf.js',
 'learn-co-students/js-from-dom-to-node-bootcamp-prep-000',
 'angular-ui/bootstrap',
 'learn-co-students/javascript-intro-to-functions-lab-bootcamp-prep-000',
 'udacity/ud851-Exercises',
 'ReactiveX/RxJava',
 'alibaba/druid',
 'apache/flink',
 'webpack/webpack',
 'grafana/grafana',
 'spmallick/learnopencv',
 'alvarotrigo/fullPage.js',
 'julycoding/The-Art-Of-Programming-By-July',
 'lib-pku/libpku',
 'lenve/vhr',
 'bilibili/ijkplayer',
 'GoogleChrome/lighthouse',
 'FFmpeg/FFmpeg',
 'github/opensource.guide',
 'yiisoft/yii2',
 'github/explore',
 'awesomedata/awesome-public-datasets',
 'fatedier/frp',
 'impress/impress.js',
 'firebase/quickstart-android',
 'discourse/discourse',
 'prakhar1989/awesome-courses',
 'cocos2d/cocos2d-x',
 'justjavac/awesome-wechat-weapp',
 'woocommerce/woocommerce',
 'phonegap/phonegap-start',
 'crossoverJie/JCSprout',
 'rust-lang/rust',
 'qiubaiying/qiubaiying.github.io',
 'fengdu78/Coursera-ML-AndrewNg-Notes',
 'arduino/Arduino',
 'axios/axios',
 'soimort/you-get',
 'CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers',
 'apache/incubator-mxnet',
 'huggingface/transformers',
 'adobe/brackets',
 'moment/moment',
 'judasn/IntelliJ-IDEA-Tutorial',
 'grpc/grpc',
 'square/retrofit',
 'akveo/ngx-admin',
 'etcd-io/etcd',
 'swirldev/swirl_courses',
 'jrowberg/i2cdevlib',
 'sahat/hackathon-starter',
 'forezp/SpringCloudLearning',
 'apache/airflow',
 'Micropoor/Micro8',
 'dcloudio/mui',
 'deadlyvipers/dojo_rules',
 'google-research/bert',
 'apache/hadoop',
 'learn-co-students/js-functions-lab-bootcamp-prep-000',
 'OAI/OpenAPI-Specification',
 'tesseract-ocr/tesseract']
 

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        return repo_info.get("language", None)
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_contents = requests.get(get_readme_download_url(contents)).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data2.json", "w"), indent=1)
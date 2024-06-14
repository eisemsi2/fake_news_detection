const express = require('express');
const bodyParser = require('body-parser');
const { spawnSync } = require('child_process');
const {getSomeLinks, getArtilce} = require('./webscrap');
const { Axios, AxiosError } = require('axios');

const app = express();

app.use(bodyParser.json());


app.post('/predict',async (req, res) =>  {
    let start = new Date().getTime();
    const article = req.body.article;
    const links = await getSomeLinks(article);
    let end = new Date().getTime();

    console.log('Time taken to get links: ', end-start);
    console.log(links);
    start = new Date().getTime();
    const process = spawnSync('python3', ['prediction.py', article]);
    const result = process.stdout?.toString()?.trim();
    const error = process.stderr?.toString()?.trim();
    end = new Date().getTime();
    console.log('Time taken to get prediction: ', end-start);
    if (!result) {
        res.json({"error" : error});
        return;
    }
    let score = 0.5;
    start = new Date().getTime();
    for(let i=0; i<links.length; i++) {
        const article2 = await getArtilce(links[i]);
        if (article2 === "error") {
            continue;
        }
        console.log(links[i]);
        console.log(article2);
        const process2 = spawnSync('python3', ['verifyarticle.py', article, article2]);
        const result2 = process2.stdout?.toString()?.trim();
        const error2 = process2.stderr?.toString()?.trim();
        if (result2) {
            console.log(result2);
            score = parseFloat(result2);
            break;
        }
    }
    end = new Date().getTime();
    console.log('Time taken to verify articles: ', end-start);
    res.json({result ,score});
});

app.listen(3000,() => {
    console.log('server running at http://localhost:3000/');
})
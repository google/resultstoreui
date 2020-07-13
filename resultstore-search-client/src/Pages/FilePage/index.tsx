import React, { useEffect, useState, useContext } from 'react';
import { RouteComponentProps } from 'react-router-dom';
import { useGoogleLogin } from 'react-google-login';
import { downloadFile, DownloadFileCallback } from '../../api/client/client';
import * as QueryString from 'query-string';
import { AuthContext } from '../../contexts/AuthContext';
import config from '../../config/ConfigLoader';

interface State {
    fileData: any;
}

const FilePage = ({ location }: RouteComponentProps) => {
    const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);
    const authContext = useContext(AuthContext);
    const logIn = (response) => {
        authContext.setTokenId(response.tokenObj.id_token);
        setIsLoggedIn(true);
    };
    useGoogleLogin({
        isSignedIn: true,
        onSuccess: logIn,
        onFailure: () => {},
        clientId: config.clientId,
    });
    const [fileData, setFileData] = useState<State['fileData']>('');
    const qs = QueryString.parse(location.search);
    const fileName = qs.fileName as string;
    const prefix = qs.prefix as string;
    const fullFileLocation = `${prefix}/${fileName}`;

    useEffect(() => {
        const formatResponse = (data: string) => {
            const splitFileName = fileName.split('.');
            if (splitFileName[splitFileName.length - 1] === 'json') {
                return `<pre>${JSON.stringify(
                    JSON.parse(data),
                    null,
                    2
                )}</pre>`;
            } else {
                return data;
            }
        };

        const downloadFileCallback: DownloadFileCallback = (err, response) => {
            if (err) {
                console.error(err);
            } else {
                setFileData(formatResponse(response.getFileData()));
            }
        };

        downloadFile(
            fullFileLocation,
            authContext.tokenId,
            downloadFileCallback
        );
    }, [isLoggedIn, fullFileLocation, fileName, authContext.tokenId]);

    return <div dangerouslySetInnerHTML={{ __html: fileData }} />;
};

export default FilePage;

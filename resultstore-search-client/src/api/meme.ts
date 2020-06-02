import grpc from 'grpc';
import {ResultStoreDownloadClient} from './resultstore_download_grpc_pb';
import {SearchInvocationsRequest} from './resultstore_download_pb';

const client = new ResultStoreDownloadClient('localhost:50051',
    grpc.credentials.createInsecure());

const meme = () => {
    const request = new SearchInvocationsRequest()
    request.setPageSize(0)
    request.setQuery('invocation_attributes.user:jessepai')
    request.setProjectId('google.com:gchips-productivity')
    const metadata = new grpc.Metadata()
    metadata.add('x-goog-fieldmask', 'next_page_token,invocations.name')
    client.searchInvocations(request, metadata, (error, response) => {
        if (error) {
            console.log(error)
        } else {
            console.log(response)
        }
    })
}

export default meme
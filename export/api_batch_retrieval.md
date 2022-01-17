
---
title: Programmatic access - Batch retrieval of entries
categories: UniProtKB,UniRef,UniParc,Programmatic_access,Batch_retrieval,help
---

Entries can be retrieved in batch by querying our [Retrieve/ID mapping service](http://www.uniprot.org/help/uploadlists) with a list of UniProt identifers. Here is a [Perl example](http://www.uniprot.org/help/api_batch_retrieval#batch_retrieval_perl_example).

use strict;
use warnings;
use LWP::UserAgent;

my $list = $ARGV\[0\]; # File containg list of UniProt identifiers.

my $base = 'https://www.uniprot.org';
my $tool = 'uploadlists';

my $contact = ''; # Please set a contact email address here to help us debug in case of problems (see https://www.uniprot.org/help/privacy).
my $agent = LWP::UserAgent->new(agent => "libwww-perl $contact");
push @{$agent->requests\_redirectable}, 'POST';

my $response = $agent->post("$base/$tool/",
                            \[ 'file' => \[$list\],
                              'format' => 'txt',
                              'from' => 'ACC+ID',
                              'to' => 'ACC',
                            \],
                            'Content\_Type' => 'form-data');

while (my $wait = $response->header('Retry-After')) {
  print STDERR "Waiting ($wait)...\\n";
  sleep $wait;
  $response = $agent->get($response->base);
}

$response->is\_success ?
  print $response->content :
  die 'Failed, got ' . $response->status\_line .
    ' for ' . $response->request->uri . "\\n";

See also:  
  
[REST API - Access the UniProt website programmatically](http://www.uniprot.org/help/api) - batch retrieval, ID mapping, queries, downloads, etc
        
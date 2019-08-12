<?php
declare(strict_types=1);

namespace Leones\Concordance;

use Iterator;
use League\Csv\Reader;
use League\Csv\Writer;

class Converter
{
    private const CONCORDANCE_FILE = 'adressenconcordans.csv';
    private const COMBINED_FILE = 'adressenconcordans-combined.csv';
    private const SORTED_FILE = 'adressenconcordans-sorted.csv';
    private const DEDUPED_LOCATIONS_FILE = 'adressenconcordans-deduped.csv';
    private const UNIQUE_FILE = 'adressenconcordans-sorted.csv';

    public function run():void
    {
        $this->combineConcordanceData();
        $this->sortData();
        $this->removeIdenticalLocationPoints();
        $this->removeIdenticalAddresses();
    }

    /**
     * Step 1
     * Create one big list of all addresses from the concordance
     *
     * @throws \League\Csv\CannotInsertRecord
     */
    private function combineConcordanceData():void
    {
        $records = $this->readCsvToIterator(Helper::filePath(self::CONCORDANCE_FILE));

        $writer = Writer::createFromPath(Helper::filePath(self::COMBINED_FILE), 'w+');
        $writer->insertOne(['lp', 'straat', 'nr', 'tvg', 'string']);

        foreach ($records as $offset => $record) {
            if (strlen($record['straat1909']) > 2) {
                $addressString = $record['straat1909'] . $record['nr1909'] . $record['tvg1909'];
                $writer->insertOne([
                    $record['lp'],
                    $record['straat1909'],
                    $record['nr1909'],
                    $record['tvg1909'],
                    $addressString
                ]);
            }

            if (strlen($record['straat1876']) > 2) {
                $addressString = $record['straat1876'] . $record['nr1876'] . $record['tvg1876'];
                $writer->insertOne([
                    $record['lp'],
                    $record['straat1876'],
                    $record['nr1876'],
                    $record['tvg1876'],
                    $addressString
                ]);
            }
        }
    }

    private function readCsvToIterator(string $file): Iterator
    {
        $reader = Reader::createFromPath($file, 'r');
        $reader->setHeaderOffset(0);

        return $reader->getRecords();
    }

    /**
     * Step 2
     * Sort the data on the string column
     */
    private function sortData():void
    {
        $records = Helper::readCsvToArray(Helper::filePath(self::COMBINED_FILE));

        $strings = array_column($records, 'string');
        array_multisort($strings, SORT_ASC, $records);

        print count($records) . ' sorted items left' . PHP_EOL;
        $this->writeToCsv(self::SORTED_FILE, $records);
    }

    private function writeToCsv(string $file, array $records): void
    {
        $writer = Writer::createFromPath(Helper::filePath($file), 'w+');
        $writer->insertOne(['lp', 'straat', 'nr', 'tvg', 'string']);
        $writer->insertAll($records);
    }

    /**
     * Step 3
     * Remove second entry that has identical location points AND address as the previous one
     */
    private function removeIdenticalLocationPoints(): void
    {
        $records = Helper::readCsvToArray(Helper::filePath(self::SORTED_FILE));

        $lastItem = 'dummy';
        foreach ($records as $key => $row) {
            $lpString = $row['lp'] . $row['straat'] . $row['nr'] . $row['tvg'];
            if ($lpString === $lastItem) {
                unset($records[$key]);
                continue;
            }
            $lastItem = $lpString;
        }
        print count($records) . ' deduped items left' . PHP_EOL;
        $this->writeToCsv(self::DEDUPED_LOCATIONS_FILE, $records);
    }

    /**
     * Step 4
     * Remove all entries of identical addresses (ambiguous)
     */
    private function removeIdenticalAddresses(): void
    {
        $records = Helper::readCsvToArray(Helper::filePath(self::DEDUPED_LOCATIONS_FILE));

        $lastItem = 'dummy';
        foreach ($records as $key => $row) {
            $addressString = $row['straat'] . $row['nr'] . $row['tvg'];
            if ($addressString === $lastItem) {

                $last = $key - 1;
                $current = $key;

                unset($records[$last]);
                unset($records[$current]);
            }
            $lastItem = $addressString;
        }
        print count($records) . ' unique items left' . PHP_EOL;
        $this->writeToCsv(self::UNIQUE_FILE, $records);
    }
}
